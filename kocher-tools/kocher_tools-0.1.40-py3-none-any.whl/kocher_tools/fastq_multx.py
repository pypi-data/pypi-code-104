import os
import sys
import logging
import subprocess
import signal

from kocher_tools.misc import confirmExecutable

def assignOutput (out_path, discard_empty_output, barcode_type, r2_given):

	# Create list to hold commands
	output_list = []

	# Define the basic filename
	output_filename = os.path.join(out_path, '%%_%s.fastq.gz')

	# Check if the barcode type is i5
	if barcode_type == 'i5':

		# Discard empty output, if specified
		if discard_empty_output: output_list.extend(['-o', 'n/a']) 
		else: output_list.extend(['-o', output_filename % 'i5'])

		# Assign the i7 file
		output_list.extend(['-o', output_filename % 'i7'])

	# Check if the barcode type is i7
	elif barcode_type == 'i7':
	
		# Discard empty output, if specified
		if discard_empty_output: output_list.extend(['-o', 'n/a']) 
		else: output_list.extend(['-o', output_filename % 'i7'])

	# Assign the R1 and R2 output
	output_list.extend(['-o', output_filename % 'R1'])
	if r2_given: output_list.extend(['-o', output_filename % 'R2'])

	return output_list

def i5ReformatMap (i5_map_filename, reformatted_filename, reverse_complement_barcodes):

	# Assign the base complements, if required
	if reverse_complement_barcodes: complements = str.maketrans('ATCG','TAGC')

	# Open the reformatted file
	reformatted_i5_map = open(reformatted_filename, 'w')

	# Open the i5 map file
	with open(i5_map_filename) as i5_map_file:

		# Loop the i5 map file, line by line
		for i5_map_line in i5_map_file:

			# Split the line into: plate, barcode, and locus (if given)
			try: i5_plate, i5_barcode, i5_locus = i5_map_line.split()
			except:
				i5_plate, i5_barcode = i5_map_line.split()
				i5_locus = ''

			# Reverse complemente the barcode, if required
			if reverse_complement_barcodes: i5_barcode = i5_barcode[::-1].translate(complements)
				
			# Define the locus string
			locus_str = f'_{i5_locus}' if i5_locus else ''

			# Write to the reformatted file
			reformatted_i5_map.write(f'{i5_plate}{locus_str}\t{i5_barcode}\n')

	# Close the file
	reformatted_i5_map.close()

def i5BarcodeJob (i5_map_filename, i5_input, i7_input, r1_input, r2_input, out_path, discard_i5, reverse_complement_barcodes):

	# Define the reformatted i5 map filename
	reformatted_i5_map_filename = i5_map_filename + '.reformatted'

	# Reformat the i5 map
	i5ReformatMap(i5_map_filename, reformatted_i5_map_filename, reverse_complement_barcodes)

	# Create the basic input arg list
	multiplex_call_args = ['-B', reformatted_i5_map_filename, i5_input, i7_input, r1_input]
	if r2_input: multiplex_call_args.append(r2_input)

	# Add the output args, using the path, if empty files should be kept, and set the barcode type as i5
	multiplex_call_args.extend(assignOutput(out_path, discard_i5, 'i5', r2_input != None))

	# Call fastq-multz with the argus
	callFastqMultx(multiplex_call_args)

	# Remove the reformatted i5 map
	os.remove(reformatted_i5_map_filename)

def i7BarcodeJob (i7_map_filename, i7_input, r1_input, r2_input, out_path, discard_i7):

	# Create the basic input arg list
	multiplex_call_args = ['-B', i7_map_filename, i7_input, r1_input]
	if r2_input: multiplex_call_args.append(r2_input)

	# Add the output args, using the path, if empty files should be kept, and set the barcode type as i5
	multiplex_call_args.extend(assignOutput(out_path, discard_i7, 'i7', r2_input != None))

	# Call fastq-multz with the argus
	callFastqMultx(multiplex_call_args)

def checkFastqMultxForErrors (fastq_multx_stderr):

	# Loop the stderr line by line
	for fastq_multx_stderr_lines in fastq_multx_stderr:

		# Ignore barcode file statement
		if 'Using Barcode File:' in fastq_multx_stderr:
			pass

		# Ignore end used file statement
		elif 'End used:' in fastq_multx_stderr:
			pass

		# Ignore the skipped (due to distance) statement
		elif 'Skipped because of distance' in fastq_multx_stderr:
			pass

		# Check if there is an error
		elif 'Error:' in fastq_multx_stderr:

			# Report the error
			raise Exception(fastq_multx_stderr)

		# Check if there are other messages
		else:

			print ('Error? - %s' % fastq_multx_stderr)

def callFastqMultx (fastq_multx_call_args):

	fastq_multx_executable = confirmExecutable('fastq-multx')

	# Check if executable is installed
	if not fastq_multx_executable:
		raise IOError('fastq-multx not found. Please confirm the executable is installed')

	# fastq-multx subprocess call
	fastq_multx_call = subprocess.Popen([fastq_multx_executable] + fastq_multx_call_args, stderr = subprocess.PIPE, stdout = subprocess.PIPE, preexec_fn = lambda: signal.signal(signal.SIGPIPE, signal.SIG_DFL))

	# Get stdout and stderr from subprocess
	fastq_multx_stdout, fastq_multx_stderr = fastq_multx_call.communicate()

	# Check if code is running in python 3
	if sys.version_info[0] == 3:
		
		# Convert bytes to string
		fastq_multx_stdout = fastq_multx_stdout.decode()
		fastq_multx_stderr = fastq_multx_stderr.decode()

	# Check the stderr for errors
	checkFastqMultxForErrors(fastq_multx_stderr)
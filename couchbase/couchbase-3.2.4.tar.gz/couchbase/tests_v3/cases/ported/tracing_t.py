#
# Copyright 2013, Couchbase, Inc.
# All Rights Reserved
#
# Licensed under the Apache License, Version 2.0 (the "License")
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
from unittest import SkipTest

from flaky import flaky

import couchbase
from couchbase.exceptions import (
    DocumentNotFoundException)

from couchbase_tests.base import TracedCase, CollectionTestCase
import logging
import couchbase_core._libcouchbase
import couchbase_core._logutil
from couchbase.exceptions import TimeoutException
from time import sleep
import re
import couchbase_core
from functools import reduce
from pyparsing import *
import sys
try:
    import __builtin__ as builtins
except BaseException:
    import builtins

from datetime import timedelta


class BogusHandler:
    def __init__(self, pattern=None):
        self.records = []
        self.pattern = re.compile(pattern) if pattern else None
        self.count = 0

    def handler(self, **kwargs):
        couchbase_core._logutil.pylog_log_handler(**kwargs)
        if self.pattern and self.pattern.match(str(kwargs)):
            self.count += 1
        self.records.append(kwargs)


class EnabledByDefaultTest(CollectionTestCase):
    def setUp(self, **kwargs):
        super(EnabledByDefaultTest, self).setUp(enable_tracing=None)

    def test_tracer_enabledbydefault(self):
        self.assertTrue(self.cb.tracer)


class CanEnableTest(CollectionTestCase):
    def setUp(self, **kwargs):
        super(CanEnableTest, self).setUp(enable_tracing="true")

    def test_tracer_canenable(self):
        self.assertTrue(self.cb.tracer)


class CanDisableTest(CollectionTestCase):
    def setUp(self, **kwargs):
        super(CanDisableTest, self).setUp(enable_tracing="false")

    def test_tracer_candisable(self):
        self.assertFalse(self.cb.tracer)


class TimeoutTest(TracedCase):
    def setUp(self, *args, **kwargs):
        if not couchbase_core._libcouchbase.PYCBC_TRACING:
            raise SkipTest("Tracing feature not compiled into Python Client")
        kwargs = {}
        couchbase.enable_logging()
        kwargs['enable_tracing'] = "true"
        #super(TimeoutTest, self).setUp(**kwargs)
        super(
            TimeoutTest,
            self).setUp(
            trace_all=True,
            enable_logging=True,
            use_parent_tracer=False,
            flushcount=0)
        self.repetitions = 100
        logging.info("starting TimeoutTest")

    def test_timeout(self):
        raise SkipTest("To be fixed")
        if sys.platform == 'win32':
            raise SkipTest("To be fixed on Windows")
        if sys.version_info >= (3, 6) and sys.platform.startswith(
                'linux') and os.environ.get("VALGRIND_REPORT_DIR"):
            raise SkipTest("To be fixed on Linux 3.6/Valgrind")
        couchbase.enable_logging()
        bucket = self.coll
        bucket.upsert("key", "value")

        self.timeout = timedelta(seconds=9e-6)
        bucket.tracing_orphaned_queue_flush_interval = timedelta(seconds=1)
        bucket.tracing_orphaned_queue_size = 10
        bucket.tracing_threshold_queue_flush_interval = timedelta(seconds=5)
        bucket.tracing_threshold_queue_size = 10
        bucket.tracing_threshold_kv = timedelta(seconds=1000)
        bucket.tracing_threshold_n1ql = timedelta(seconds=1000)
        bucket.tracing_threshold_view = timedelta(seconds=1000)
        bucket.tracing_threshold_fts = timedelta(seconds=1000)
        bucket.tracing_threshold_analytics = timedelta(seconds=1000)

        self.verify_tracer(
            bucket,
            r'.*Operations over threshold:.*',
            rep_factor=100)

    def test_orphaned(self):
        raise SkipTest("To be fixed")
        if sys.version_info >= (3, 6) and sys.platform.startswith(
                'linux') and os.environ.get("VALGRIND_REPORT_DIR"):
            raise SkipTest("To be fixed on Linux 3.6/Valgrind")
        if sys.version_info >= (3, 7) and sys.platform.startswith('win'):
            raise SkipTest("To be fixed on Win 3.7")
        bucket = self.coll
        bucket.upsert("key", "value")

        self.timeout = timedelta(seconds=9e-6)
        bucket.tracing_orphaned_queue_flush_interval = timedelta(seconds=1)
        bucket.tracing_orphaned_queue_size = 10
        bucket.tracing_threshold_queue_flush_interval = timedelta(seconds=5)
        bucket.tracing_threshold_queue_size = 10
        bucket.tracing_threshold_kv = timedelta(seconds=1000)
        bucket.tracing_threshold_n1ql = timedelta(seconds=1000)
        bucket.tracing_threshold_view = timedelta(seconds=1000)
        bucket.tracing_threshold_fts = timedelta(seconds=1000)
        bucket.tracing_threshold_analytics = timedelta(seconds=1000)

        self.verify_tracer(
            bucket,
            r'.*Orphan responses observed:.*',
            rep_factor=100)

    def verify_tracer(self, bucket, pattern, rep_factor=1):
        self.trigger_tracer(bucket, self.repetitions * rep_factor, pattern)
        self.assertTrue(
            self.handler.count > 0,
            "no {} found in output {}".format(
                pattern,
                self.handler.records))
        logging.info("Finished TimeoutTest")

    def trigger_tracer(self, bucket, i, pattern, mincount=1):
        self.handler = BogusHandler(pattern=pattern)
        couchbase_core._libcouchbase.lcb_logging(self.handler.handler)

        to_ops = 0

        # first do a bunch of work in a tight loop to trigger a timeout
        for x in range(0, i):
            try:
                bucket.get("key", timeout=self.timeout)
            except TimeoutException as e:
                logging.error("Got exception [{}]".format(str(e)))
                to_ops += 1
            if self.handler.count >= mincount:
                break

        # then do more work at a low rate so we can see the Threshold Logging
        # Tracer
        for x in range(0, 10):
            sleep(1)
            try:
                bucket.get("key", timeout=self.timeout)
            except TimeoutException as e:
                logging.error("Got exception [{}]".format(str(e)))
                to_ops += 1
        logging.info('timedout ops ' + str(to_ops))
        couchbase_core._libcouchbase.lcb_logging(
            couchbase_core._logutil.pylog_log_handler)

    def tearDown(self):
        super(TimeoutTest, self).tearDown()
        couchbase.disable_logging()


class ExceptionGrammar:
    def __init__(self):
        self.grammar = self.exception_grammar()

    @staticmethod
    def gen_json_grammar():
        def make_keyword(kwd_str, kwd_value):
            return Keyword(kwd_str).setParseAction(replaceWith(kwd_value))

        TRUE = make_keyword("true", True)
        FALSE = make_keyword("false", False)
        NULL = make_keyword("null", None)

        LBRACK, RBRACK, LBRACE, RBRACE, COLON = map(Suppress, "[]{}:")

        jsonString = dblQuotedString().setParseAction(removeQuotes)
        jsonNumber = pyparsing_common.number() + Optional("L")

        jsonObject = Forward()
        jsonValue = Forward()
        jsonElements = delimitedList(jsonValue)
        jsonArray = Group(LBRACK + Optional(jsonElements, []) + RBRACK)
        jsonValue << (jsonString | jsonNumber | Group(
            jsonObject) | jsonArray | TRUE | FALSE | NULL)
        memberDef = Group(jsonString + COLON + jsonValue)
        jsonMembers = delimitedList(memberDef)
        jsonObject << Dict(LBRACE + Optional(jsonMembers) + RBRACE)

        jsonComment = cppStyleComment
        jsonObject.ignore(jsonComment)
        return jsonObject

    def delimit(self, entry, delimiter=None):
        result = entry + Suppress(delimiter or Or(",", self.terminator))
        result.skipWhitespace = True
        return result

    def opt(self, exc_entry_key, val=None, optional=True, delimiter=None):
        val = val or self.python_quoted_string
        result = Suppress(exc_entry_key) + Suppress("=") + val
        result = self.delimit(result, delimiter)
        result = Group(result)
        if optional:
            result = Optional(result)
        result.setName(exc_entry_key)
        return result

    def exception_grammar(self):
        self.python_quoted_string = Optional(
            Suppress(Or('u', 'b'))) + quotedString().setParseAction(removeQuotes)
        self.terminator = ">"
        self.jsonobject = ExceptionGrammar.gen_json_grammar()
        bracketed_text = Suppress(
            "(") + OneOrMore(CharsNotIn(')')) + Suppress(")")
        square_bracketed_text = Suppress(
            "[") + Regex(r'[^\]]+') + Suppress("]")
        hex_str = Suppress("0x") + pyparsing_common.hex_integer

        rc_value = hex_str + square_bracketed_text
        opt_message = Optional(self.delimit(
            OneOrMore(And(CharsNotIn(','), CharsNotIn(' ')))))
        tracing_output = self.opt(
            "Tracing Output",
            val=self.jsonobject,
            delimiter=self.terminator)

        entries = [self.opt("Key"),
                   self.opt("RC", val=rc_value),
                   opt_message,
                   self.opt("Results", pyparsing_common.integer),
                   self.opt("C Source",
                            val=bracketed_text)] + \
            list(map(self.opt, ["Obj", "Context", "Ref"])) + \
            [tracing_output]
        exception_dict = Suppress('<') + reduce(ParserElement.__add__, entries)
        exception_dict.skipWhitespace = True
        return exception_dict

    def parse_exception(self, cb_exc):
        exception_str = str(cb_exc)

        parsed_exception = self.grammar.parseString(exception_str)
        parsed_exception[-1] = parsed_exception[-1].asDict()
        return parsed_exception


exception_grammar = ExceptionGrammar()


class TracingTest(TracedCase):

    def setUp(self, *args, **kwargs):
        if not couchbase_core._libcouchbase.PYCBC_TRACING:
            raise SkipTest("Tracing feature not compiled into Python Client")
        pass

    def test_threshold_multi_get(self):
        super(
            TracingTest,
            self).setUp(
            trace_all=True,
            enable_logging=True,
            use_parent_tracer=False,
            flushcount=0)
        raise SkipTest("to be fixed")
        super(
            TracingTest,
            self).setUp(
            trace_all=True,
            enable_logging=True,
            use_parent_tracer=False,
            flushcount=0)
        error_message_expected = r'.*Operations over threshold:.*'
        handler = BogusHandler(error_message_expected)
        couchbase_core._libcouchbase.lcb_logging(handler.handler)

        kv = self.gen_kv_dict(amount=3, prefix='get_multi')
        for i in range(0, 500000):
            rvs = self.coll.upsert_multi(kv)
            self.assertTrue(rvs.all_ok)

            k_subset = list(kv.keys())[:2]

            rvs1 = self.coll.get_multi(k_subset)
            self.assertEqual(len(rvs1), 2)
            self.assertEqual(rvs1[k_subset[0]].value, kv[k_subset[0]])
            self.assertEqual(rvs1[k_subset[1]].value, kv[k_subset[1]])

            rv2 = self.coll.get_multi(kv.keys())
            self.assertEqual(rv2.keys(), kv.keys())
        self.flush_tracer()

        self.assertTrue(
            handler.count > 0,
            "no {} found in logs".format(error_message_expected))

    @flaky(10, 1)
    def test_tracing_result_context(self):
        super(
            TracingTest,
            self).setUp(
            trace_all=True,
            enable_logging=True,
            use_parent_tracer=False,
            flushcount=0)
        raise SkipTest("to be fixed")
        kv_missing = self.gen_kv_dict(amount=3, prefix='multi_missing_mixed')
        kv_existing = self.gen_kv_dict(amount=3, prefix='multi_existing_mixed')

        logging.getLogger().setLevel(logging.DEBUG)

        self.coll.remove_multi(list(kv_missing.keys()) + list(kv_existing.keys()),
                               quiet=True)

        self.coll.upsert_multi(kv_existing)

        rvs = self.coll.get_multi(
            list(kv_existing.keys()) + list(kv_missing.keys()),
            quiet=True)

        self.assertFalse(rvs.all_ok)

        for k, v in kv_missing.items():
            self.assertTrue(k in rvs)
            self.assertFalse(rvs[k].success)
            self.assertTrue(rvs[k].content is None)
            self.assertTrue(
                DocumentNotFoundException._can_derive(
                    rvs[k].error))
        self.verify_tracing_output(kv_existing, rvs, True)
        # Try this again, but without quiet
        cb_exc = None
        try:
            self.coll.get_multi(
                list(
                    kv_existing.keys()) +
                list(
                    kv_missing.keys()))
        except DocumentNotFoundException as e:
            cb_exc = e

        if os.getenv("PYCBC_CHECK_TRACING_FULL"):
            # TODO: fix - https://issues.couchbase.com/browse/PYCBC-889
            self.assertTrue(cb_exc)
            all_res = cb_exc.all_results
            self.assertTrue(all_res)
            self.assertFalse(all_res.all_ok)

            self.verify_exception_string(cb_exc, kv_missing, rvs)
            logging.error(cb_exc)
            self.verify_tracing_output(kv_existing, all_res, True)
            self.verify_tracing_output(kv_missing, all_res, False)

        del cb_exc

    @staticmethod
    def filter_tracing_output(x):
        return {k: v for k, v in x.items() if k not in {'i', 'c', 'FILE',
                                                        'FUNC', 'LINE', 'debug_info'}}

    def verify_exception_string(self, cb_exc, kv_missing, rvs):
        parsed_exception = exception_grammar.parse_exception(cb_exc)
        import logging
        logging.error(
            'got exception {}, \nparsed as {}'.format(
                str(cb_exc), parsed_exception))
        logging.error('original output is {}'.format(rvs))
        parsed_exception_tracing_output = parsed_exception[-1]
        for key, value in kv_missing.items():
            self.assertIn(key, parsed_exception_tracing_output.keys())
            parsed_exception_tracing_output_for_key = parsed_exception_tracing_output[key]
            self.verify_output(parsed_exception_tracing_output_for_key)

            self.assertEqual(TracingTest.filter_tracing_output(rvs[key].tracing_output),
                             TracingTest.filter_tracing_output(parsed_exception_tracing_output_for_key))

    def verify_tracing_output(self, kv_set, rvs, is_existing):
        for k, v in kv_set.items():
            tracing_output = rvs[k]._tracing_output
            self.verify_output(tracing_output)
            self.assertTrue(k in rvs)
            self.assertEqual(rvs[k].success, is_existing)
            self.assertEqual(rvs[k].content, v if is_existing else None)
            if is_existing:
                self.assertTrue(rvs[k].success)

    def verify_output(self, tracing_output):
        bucket_name = "default"
        expected_tracing = {'s': r'.+:.+', 'b': bucket_name, 'c': r'[0-9a-f]+/[0-9a-f]+', 'l': r'.+:.+', 'r': r'.+:.+',
                            't': lambda v: self.assertEqual(v, self.timeout.total_seconds() * 1000000) if self.timeout else None,
                            'i': lambda v: self.assertIn(type(v), [int, getattr(builtins, 'long', None), float])}
        exceptions = []
        for label, pattern in expected_tracing.items():
            value = tracing_output.get(label)
            try:
                self.assertIsNotNone(
                    value, "{label} of {output} yields None".format(
                        label=label, output=tracing_output))
                if isinstance(pattern, str):
                    self.assertRegex(value, pattern)
                else:
                    pattern(value)
            except Exception as e:
                exceptions.append(e)
                raise e

        if len(exceptions) > 0:
            raise self.failureException(
                "Got exceptions: {}".format(
                    str(exceptions)))

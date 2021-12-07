# Copyright 2019 Katteli Inc.
# TestFlows.com Open-Source Software Testing Framework (http://testflows.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import threading
import subprocess
import tempfile

import testflows._core.cli.arg.type as argtype

from testflows._core.cli.arg.common import epilog
from testflows._core.cli.arg.common import HelpFormatter
from testflows._core.cli.arg.handlers.handler import Handler as HandlerBase
from testflows._core.message import Message
from testflows._core.transform.log.pipeline import Pipeline as PipelineBase
from testflows._core.transform.log.read_and_filter import transform as read_and_filter_transform
from testflows._core.transform.log.nice import transform as nice_transform
from testflows._core.transform.log.parse import transform as parse_transform
from testflows._core.transform.log.write import transform as write_transform
from testflows._core.transform.log.stop import transform as stop_transform

class Handler(HandlerBase):
    @classmethod
    def add_command(cls, commands):
        parser = commands.add_parser("messages", help="messages", epilog=epilog(),
            description="Show messages.",
            formatter_class=HelpFormatter)

        parser.add_argument("name", metavar="name", type=str, help="test name", default=".*?", nargs="?")
        parser.add_argument("--log", metavar="input", type=argtype.logfile("r", bufsize=1, encoding="utf-8"),
                nargs="?", help="input log, default: stdin", default="-")
        parser.add_argument("--output", metavar="output", type=argtype.file("w", bufsize=1, encoding="utf-8"),
                nargs="?", help='output, default: stdout', default="-")
        format_choices = ["nice", "raw"]
        parser.add_argument("--format", "-f", metavar="name", type=str, choices=format_choices,
            default="nice", help=f"output format, choices are {format_choices}, default: nice")
        parser.set_defaults(func=cls())

    class Pipeline(PipelineBase):
        def __init__(self, name, input, output, format=None, tail=False):
            stop_event = threading.Event()
            command = f"grep -E \',\"test_name\":\"%s'" % name

            steps = [
                read_and_filter_transform(input, command=command, stop=stop_event, tail=tail)
            ]

            if format != "raw":
                steps += [parse_transform()]

            if format == "nice":
                steps += [
                    nice_transform()
                ]

            steps.append(write_transform(output))
            steps.append(stop_transform(stop_event))

            super(Handler.Pipeline, self).__init__(steps, stop=stop_event)

    def handle(self, args):
        self.Pipeline(args.name.replace("'", r"'\''"), args.log, args.output, args.format).run()

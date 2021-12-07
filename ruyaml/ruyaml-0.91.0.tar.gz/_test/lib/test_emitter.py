from __future__ import absolute_import, print_function

# Skipped because we have no idea where all those fixtures originate
import pytest

import ruyaml as yaml

pytestmark = pytest.mark.skip


def _compare_events(events1, events2):
    assert len(events1) == len(events2), (events1, events2)
    for event1, event2 in zip(events1, events2):
        assert event1.__class__ == event2.__class__, (event1, event2)
        if isinstance(event1, yaml.NodeEvent):
            assert event1.anchor == event2.anchor, (event1, event2)
        if isinstance(event1, yaml.CollectionStartEvent):
            assert event1.tag == event2.tag, (event1, event2)
        if isinstance(event1, yaml.ScalarEvent):
            if True not in event1.implicit + event2.implicit:
                assert event1.tag == event2.tag, (event1, event2)
            assert event1.value == event2.value, (event1, event2)


def test_emitter_on_data(data_filename, canonical_filename, verbose=False):
    with open(data_filename, 'rb') as fp0:
        events = list(yaml.parse(fp0))
    output = yaml.emit(events)
    if verbose:
        print('OUTPUT:')
        print(output)
    new_events = list(yaml.parse(output))
    _compare_events(events, new_events)


test_emitter_on_data.unittest = ['.data', '.canonical']


def test_emitter_on_canonical(canonical_filename, verbose=False):
    with open(canonical_filename, 'rb') as fp0:
        events = list(yaml.parse(fp0))
    for canonical in [False, True]:
        output = yaml.emit(events, canonical=canonical)
        if verbose:
            print('OUTPUT (canonical=%s):' % canonical)
            print(output)
        new_events = list(yaml.parse(output))
        _compare_events(events, new_events)


test_emitter_on_canonical.unittest = ['.canonical']


def test_emitter_styles(data_filename, canonical_filename, verbose=False):
    for filename in [data_filename, canonical_filename]:
        with open(filename, 'rb') as fp0:
            events = list(yaml.parse(fp0))
        for flow_style in [False, True]:
            for style in ['|', '>', '"', "'", ""]:
                styled_events = []
                for event in events:
                    if isinstance(event, yaml.ScalarEvent):
                        event = yaml.ScalarEvent(
                            event.anchor,
                            event.tag,
                            event.implicit,
                            event.value,
                            style=style,
                        )
                    elif isinstance(event, yaml.SequenceStartEvent):
                        event = yaml.SequenceStartEvent(
                            event.anchor,
                            event.tag,
                            event.implicit,
                            flow_style=flow_style,
                        )
                    elif isinstance(event, yaml.MappingStartEvent):
                        event = yaml.MappingStartEvent(
                            event.anchor,
                            event.tag,
                            event.implicit,
                            flow_style=flow_style,
                        )
                    styled_events.append(event)
                output = yaml.emit(styled_events)
                if verbose:
                    print(
                        'OUTPUT (filename=%r, flow_style=%r, style=%r)'
                        % (filename, flow_style, style)
                    )
                    print(output)
                new_events = list(yaml.parse(output))
                _compare_events(events, new_events)


test_emitter_styles.unittest = ['.data', '.canonical']


class EventsLoader(yaml.Loader):
    def construct_event(self, node):
        if isinstance(node, yaml.ScalarNode):
            mapping = {}
        else:
            mapping = self.construct_mapping(node)
        class_name = str(node.tag[1:]) + 'Event'
        if class_name in [
            'AliasEvent',
            'ScalarEvent',
            'SequenceStartEvent',
            'MappingStartEvent',
        ]:
            mapping.setdefault('anchor', None)
        if class_name in ['ScalarEvent', 'SequenceStartEvent', 'MappingStartEvent']:
            mapping.setdefault('tag', None)
        if class_name in ['SequenceStartEvent', 'MappingStartEvent']:
            mapping.setdefault('implicit', True)
        if class_name == 'ScalarEvent':
            mapping.setdefault('implicit', (False, True))
            mapping.setdefault('value', "")
        value = getattr(yaml, class_name)(**mapping)
        return value


# if Loader is not a composite, add this function
# EventsLoader.add_constructor = yaml.constructor.Constructor.add_constructor


EventsLoader.add_constructor(None, EventsLoader.construct_event)


def test_emitter_events(events_filename, verbose=False):
    with open(events_filename, 'rb') as fp0:
        events = list(yaml.load(fp0, Loader=EventsLoader))
    output = yaml.emit(events)
    if verbose:
        print('OUTPUT:')
        print(output)
    new_events = list(yaml.parse(output))
    _compare_events(events, new_events)


if __name__ == '__main__':
    import test_appliance

    test_appliance.run(globals())

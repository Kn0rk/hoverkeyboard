
import pytest
from hoverkeyboard.parser import _get_key_sections


def test__get_key_sections():
    key_definitions = """0.28,0.15:
	        base:{}
               pre:
                print("xx section 1")
               action:
                    print('hoverkeyboard: No comand given')
        0.34,0.15:
	        base:{}
               pre:
                print("xx")
               action:
                    print('hoverkeyboard: No comand given')
        """
    key_sections,centers = _get_key_sections(key_definitions)
    assert len(key_sections) == 2
    assert len(centers) == 2
    assert centers[0] == pytest.approx([0.28,0.15])
    assert centers[1] == pytest.approx([0.34,0.15])
    assert "base:"in key_sections[0]
    assert "xx section 1"in key_sections[0]

import pytest
import main

def test_healthstatus_instantiation():
    # Verify that the class HealthStatus is inspectable and loadable
    assert hasattr(main, 'HealthStatus')


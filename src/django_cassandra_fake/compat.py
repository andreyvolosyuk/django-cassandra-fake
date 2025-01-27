"""Handle package compatibility."""

try:
    from dse import cqlengine
    from dse.cluster import Session
    from dse.cqlengine import columns, connection, CQLEngineException, query
    from dse.auth import PlainTextAuthProvider
    from dse.cqlengine.management import create_keyspace_simple, drop_keyspace, get_create_type
    from dse.cqlengine.models import (
        ModelMetaClass, ModelException, ColumnDescriptor,
        ModelDefinitionException, BaseModel, Model
    )
    from dse.util import OrderedDict
except ImportError:
    try:
        from cassandra import cqlengine
        from cassandra.cluster import Session
        from cassandra.cqlengine import columns, connection, CQLEngineException, query
        from cassandra.auth import PlainTextAuthProvider
        from cassandra.cqlengine.management import create_keyspace_simple, drop_keyspace, get_create_type
        from cassandra.cqlengine.models import (
            ModelMetaClass, ModelException, ColumnDescriptor,
            ModelDefinitionException, BaseModel, Model
        )
        from cassandra.util import OrderedDict
    except ImportError:
            raise ImportError('You must install either dse-driver or '
                              + 'cassandra-driver!')

from django_cassandra_fake.base import management
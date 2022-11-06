import pytest

from neodantic.engine import Database


@pytest.mark.parametrize("protocol", ["bolt", "bolt+ssc", "neo4j", "neo4j+ssc"])
async def test_connection(protocol):
    db = Database(f"{protocol}://localhost:7687", auth=("neo4j", "neo4j"))
    result = await db.check_connection()
    assert result

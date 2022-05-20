from sqlalchemy import create_engine
from sqlalchemy import text


def drop_chance_of_item_by_id(engine: object, it_id: int) -> str:
    """
    Queries the PEQ db for the drop chance of an item by its item id
    """
    stmt = text("""
    SELECT ld.item_id, i.name, s.zone, npc.name, lte.mindrop, lte.droplimit, ld.chance
    FROM lootdrop_entries AS ld
    INNER JOIN items AS i
    ON ld.item_id = i.id
    INNER JOIN loottable_entries AS lte
    ON ld.lootdrop_id = lte.lootdrop_id
    INNER JOIN npc_types AS npc
    ON lte.loottable_id = npc.loottable_id
    INNER JOIN spawnentry AS se
    ON npc.id = se.npcID
    INNER JOIN spawn2 AS s
    ON se.spawngroupID = s.spawngroupID
    INNER JOIN zone AS z
    ON s.zone = z.short_name
    WHERE s.enabled = '1' AND i.id ='19285' AND z.min_status < '1'
    ORDER BY 7 DESC
    """)
    with engine.connect() as conn:
        res = conn.execute(stmt)
        return res

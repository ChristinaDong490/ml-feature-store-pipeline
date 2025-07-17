
from datetime import timedelta
from feast import (
    Entity,
    FeatureView,
    Field,
    FileSource,
    ValueType,
)
from feast.types import Float32, Int64, String

athlete = Entity(name="athlete_id", join_keys=["athlete_id"])

file_source = FileSource(
    path="/Users/christinadong/Documents/MLops/ml-feature-store-pipeline/data/athletes_clean.parquet",
    timestamp_field="event_timestamp",
)

athlete_v1_view = FeatureView(
    name="athlete_v1_view",
    entities=[athlete],
    ttl=timedelta(days=365),
    schema=[
        Field(name="age", dtype=Int64),
        Field(name="height", dtype=Float32),
        Field(name="weight", dtype=Float32),
        Field(name="gender", dtype=Int64), # 0 or 1
        Field(name="deadlift", dtype=Float32),
        Field(name="candj", dtype=Float32),
        Field(name="snatch", dtype=Float32),
        Field(name="backsq", dtype=Float32),
    ],
    source=file_source,
)

athlete_v2_view = FeatureView(
    name="athlete_v2_view",
    entities=[athlete],
    ttl=timedelta(days=365),
    schema=[
        Field(name="bmi", dtype=Float32),
        Field(name="age", dtype=Int64),
        Field(name="gender", dtype=String),
        Field(name="region", dtype=String),
    ],
    source=file_source,
)

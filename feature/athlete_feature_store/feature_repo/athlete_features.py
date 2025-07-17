from feast import FeatureView, Field, FileSource, Entity, ValueType
from feast.types import Float32, Int64, String

athlete_entity = Entity(
    name="athlete_id",
    value_type=ValueType.STRING, 
    description="Unique identifier for an athlete"
)

athlete_v1_file_source = FileSource(
    path="/Users/christinadong/Documents/MLops/ml-feature-store-pipeline/data/feature_v1.parquet",
    timestamp_field="event_timestamp"
)

athlete_feature_view_v1 = FeatureView(
    name="athlete_demographics_v1",
    entities=[athlete_entity],
    ttl=None, 
    source=athlete_v1_file_source,
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
)
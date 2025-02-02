import great_expectations as gx
import great_expectations.expectations as gxe
import pandas as pd

context = gx.get_context()

data_source_name = "my_data_source1"
data_source = context.data_sources.add_pandas(name=data_source_name)
assert data_source.name == data_source_name

data_asset_name = "my_dataframe_data_asset1"
data_asset = data_source.add_dataframe_asset(name=data_asset_name)

batch_definition_name = "my_batch_definition1"
batch_definition = data_asset.add_batch_definition_whole_dataframe(
    batch_definition_name
)

dataframe = pd.read_csv("db\desempenho_funcionarios.csv")
batch_parameters = {"dataframe": dataframe}

# Create an Expectation to test
expectation = gx.expectations.ExpectColumnValuesToBeBetween(
    column="Treinamentos_Completos", max_value=15, min_value=0
)

# Get the dataframe as a Batch
batch = batch_definition.get_batch(batch_parameters=batch_parameters)

# Test the Expectation
validation_results = batch.validate(expectation)
print(validation_results)


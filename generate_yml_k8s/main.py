from GeneratorYml import GeneratorController


job_object = [{'name': 'A1', 'value': 'V1'}, {'name': 'A2', 'value': 'V2'}]

file_job_yml = GeneratorController().generateJobYml(job_object)


print("\n\n")
print(file_job_yml)
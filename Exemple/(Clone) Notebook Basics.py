# Databricks notebook source
print("Hello Python!")

# COMMAND ----------

# MAGIC %sql
# MAGIC select 'Hello SQL --'

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM demo_tmp_vw

# COMMAND ----------

# MAGIC %run ./Includes/Classroom-Setup-01.2

# COMMAND ----------

# MAGIC %sql 
# MAGIC SELECT * FROM demo_tmp_vw

# COMMAND ----------

print(f"DA:                   {DA}")
print(f"DA.username:          {DA.username}")
print(f"DA.paths.working_dir: {DA.paths.working_dir}")
print(f"DA.schema_name:       {DA.schema_name}")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT '${da.username}' AS current_username,
# MAGIC        '${da.paths.working_dir}' AS working_directory,
# MAGIC        '${da.schema_name}' as schema_name

# COMMAND ----------

path = f"{DA.paths.datasets}"
dbutils.fs.ls(path)

# COMMAND ----------

path = f"{DA.paths.datasets}"
files = dbutils.fs.ls(path)
display(files)

# COMMAND ----------

DA.cleanup()

# COMMAND ----------



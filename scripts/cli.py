import argparse

parser = argparse.ArgumentParser()

# Parse arguments using argparse:
#     Commands:
#         fetch <container_number>   -> call fetch_and_store_container()
#         list                       -> call query_all_containers()
#         get <container_number>     -> call query_container_by_number()

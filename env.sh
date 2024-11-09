# To inject environment variables, create ./env.py, for example with the code:
#
#   from pathlib import Path
#   import os
#
#   base_dir = Path(__file__).parent
#   os.environ['DOCKER_CONFIG'] = str(base_dir / 'tmp/docker-config')
#
#
# The environments variables will then be available, for example:
#
#   $ bin/liquidcore run python -c 'import os; print(os.environ["DOCKER_CONFIG"])'

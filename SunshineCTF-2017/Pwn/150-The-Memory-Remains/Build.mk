TARGET := the_memory_remains 
# CFLAGS := -ggdb
# OFLAGS := -O0

# Docker configuration
DOCKER_IMAGE := the_memory_remains
DOCKER_RUN_ARGS := --read-only
DOCKER_PORTS := 20002

# Only the binary is available for download
PUBLISH := $(TARGET)

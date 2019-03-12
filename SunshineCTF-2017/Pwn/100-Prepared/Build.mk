TARGET := prepared

# Docker configuration
DOCKER_IMAGE := prepared
DOCKER_PORTS := 20001
DOCKER_RUN_ARGS := --read-only

# Only the binary is available for download
PUBLISH := $(TARGET)

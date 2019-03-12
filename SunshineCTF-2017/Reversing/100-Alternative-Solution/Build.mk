TARGET := alternative_solution

# Only publish the executable
PUBLISH := $(TARGET)

DOCKER_IMAGE := alternative_solution
DOCKER_RUN_ARGS := --read-only
DOCKER_PORTS := 10001

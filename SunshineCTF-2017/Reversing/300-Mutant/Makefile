# Executable name
TARGET := mutant

# Build paths
BUILD := build
SRCS := main.c encrypt.asm
OBJS := $(patsubst %,$(BUILD)/%.o,$(SRCS))

# Compiler options
CC := gcc
CFLAGS :=

# Assembler options
AS := nasm
ASFLAGS := -f elf64

# Linker options
LD := gcc
LDFLAGS :=

# Stripping options
STRIP := strip
STRIPFLAGS :=


# Print all commands executed when VERBOSE is defined with `make VERBOSE=1`
ifdef VERBOSE
_v :=
else
_v := @
endif


all: $(TARGET)

# Stripping rule
$(TARGET): $(BUILD)/$(TARGET).raw
	@echo 'Stripping $@ <== $<'
	$(_v)$(STRIP) $(STRIPFLAGS) -o $@ $<

# Linker rule
$(BUILD)/$(TARGET).raw: $(OBJS)
	@echo 'Linking $@ <== $^'
	$(_v)$(LD) $(LDFLAGS) -o $@ $^

# Compiler rule
$(BUILD)/%.c.o: %.c | $(BUILD)/.dir
	@echo 'Compiling $@ <== $<'
	$(_v)$(CC) $(CFLAGS) -MD -MP -MF $(BUILD)/$*.c.d -c -o $@ $<

# Assembler rule
$(BUILD)/%.asm.o: %.asm | $(BUILD)/.dir
	@echo 'Assembling $@ <== $<'
	$(_v)$(AS) $(ASFLAGS) -o $@ $<


# Build dependency rules
-include $(DEPS)


# Make sure that the .dir files aren't automatically deleted after building
.SECONDARY:

%/.dir:
	$(_v)mkdir -p $* && touch $@

clean:
	@echo 'Removing built products: $(BUILD) $(TARGET)'
	$(_v)rm -rf $(BUILD) $(TARGET)

.PHONY: all clean

# Disable stupid built-in rules
MAKEFLAGS += --no-builtin-rules
.SUFFIXES:

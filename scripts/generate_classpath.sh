#!/bin/bash
# Script to generate Eclipse .classpath file for JDTLS with Bazel

# Find Bazel cache directory
BAZEL_OUTPUT=$(bazel info output_base 2>/dev/null)
if [ -z "$BAZEL_OUTPUT" ]; then
    echo "Error: Could not determine Bazel output directory"
    exit 1
fi

# Find JUnit JAR
JUNIT_JAR=$(find "$BAZEL_OUTPUT/external" -name "junit-4.*.jar" 2>/dev/null | head -1)
HAMCREST_JAR=$(find "$BAZEL_OUTPUT/external" -name "hamcrest-core-*.jar" 2>/dev/null | head -1)

if [ -z "$JUNIT_JAR" ]; then
    echo "Warning: JUnit JAR not found. Running 'bazel build //java/...' to fetch dependencies..."
    bazel build //java/...
    JUNIT_JAR=$(find "$BAZEL_OUTPUT/external" -name "junit-4.*.jar" 2>/dev/null | head -1)
    HAMCREST_JAR=$(find "$BAZEL_OUTPUT/external" -name "hamcrest-core-*.jar" 2>/dev/null | head -1)
fi

# Generate .classpath file
cat > .classpath << EOF
<?xml version="1.0" encoding="UTF-8"?>
<classpath>
EOF

# Add all java source directories
for dir in java/*/; do
    if [ -d "$dir" ]; then
        echo "	<classpathentry kind=\"src\" path=\"${dir%/}\"/>" >> .classpath
    fi
done

# Add JRE container and libraries
cat >> .classpath << EOF
	<classpathentry kind="con" path="org.eclipse.jdt.launching.JRE_CONTAINER/org.eclipse.jdt.internal.debug.ui.launcher.StandardVMType/JavaSE-17"/>
EOF

if [ -n "$JUNIT_JAR" ]; then
    echo "	<classpathentry kind=\"lib\" path=\"$JUNIT_JAR\"/>" >> .classpath
fi

if [ -n "$HAMCREST_JAR" ]; then
    echo "	<classpathentry kind=\"lib\" path=\"$HAMCREST_JAR\"/>" >> .classpath
fi

cat >> .classpath << EOF
	<classpathentry kind="output" path="bazel-bin"/>
</classpath>
EOF

echo "Generated .classpath with:"
echo "  - JUnit: $JUNIT_JAR"
echo "  - Hamcrest: $HAMCREST_JAR"
echo "  - Source directories: $(ls -d java/*/ 2>/dev/null | wc -l) found"
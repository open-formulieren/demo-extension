# Stage 1 - Build demo extension environment
FROM python:3.8-slim-buster AS demo-extension-build

WORKDIR /app

RUN pip install pip -U
COPY . /app
RUN pip install .


# Stage 2 - Build the production image with the demo extension
FROM openformulieren/open-forms:test_demo_extension AS production-build

WORKDIR /app

# Copy the dependencies of the demo-extension
COPY --from=demo-extension-build /usr/local/lib/python3.8 /usr/local/lib/python3.8

# Add demo_extension code to the image
COPY --chown=maykin:root ./demo_extension /app/src/demo_extension

USER maykin









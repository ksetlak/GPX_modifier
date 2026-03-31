i=1; for f in generated_gpx/*(N); do \
  dir=$(printf "%02d" $(( (i-1)/15 + 1 ))); \
  mkdir -p "$dir"; \
  mv "$f" "$dir/"; \
  ((i++)); \
done
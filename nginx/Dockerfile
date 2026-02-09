# Use official nginx alpine image
FROM nginx:1.24-alpine

# Remove default nginx configuration
RUN rm /etc/nginx/conf.d/default.conf

# Copy custom nginx configuration
COPY nginx.conf /etc/nginx/conf.d/app.conf

# Create non-root user (nginx already runs as nginx user in alpine)
# Just ensure permissions are correct
RUN chown -R nginx:nginx /etc/nginx/conf.d

# Expose port 80
EXPOSE 80

# Nginx runs as non-root by default in alpine image

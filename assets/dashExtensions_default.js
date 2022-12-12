window.dashExtensions = Object.assign({}, window.dashExtensions, {
    default: {
        function0: function(feature, latlng, context) {
            // Check if station is selected
            const selected = context.props.hideout.includes(feature.properties.name);
            // Display selected station in green
            if (selected) {
                return L.circleMarker(latlng, {
                    color: 'green'
                });
            }
            // Display non-selected stations in grey
            return L.circleMarker(latlng, {
                color: 'grey'
            });
        }
    }
});
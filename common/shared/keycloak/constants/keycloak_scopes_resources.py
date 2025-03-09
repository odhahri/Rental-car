keycloak_scopes_resources: dict = {
    'client': {
        'scopes': {
            'GET': 'scopes:view',
            'POST': 'scopes:create',
            'PUT': 'scopes:update',
            'DELETE': 'scopes:delete'
        },
        'resource': 'res:client'
    },

    
}

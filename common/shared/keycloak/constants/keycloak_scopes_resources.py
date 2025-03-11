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
    'car': {
        'scopes': {
            'GET': 'scopes:view',
            'POST': 'scopes:create',
            'PUT': 'scopes:update',
            'DELETE': 'scopes:delete'
        },
        'resource': 'res:car'
    },
    'agent': {
        'scopes': {
            'GET': 'scopes:view',
            'POST': 'scopes:create',
            'PUT': 'scopes:update',
            'DELETE': 'scopes:delete'
        },
        'resource': 'res:agent'
    },
    'reservation': {
        'scopes': {
            'GET': 'scopes:view',
            'POST': 'scopes:create',
            'PUT': 'scopes:update',
            'DELETE': 'scopes:delete'
        },
        'resource': 'res:reservation'
    },

    
}

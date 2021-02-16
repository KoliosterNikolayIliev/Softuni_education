function solve() {
    const proto = {};
    const instance =Object.create(proto);

    instance.extend = function (templates) {
        Object.entries(templates).forEach(createProto);

        function createProto([key, value]) {
            if (typeof value === 'function') {
                proto[key] = value;
            } else {
                instance[key] = value;
            }
        }
    };
    return instance;
}
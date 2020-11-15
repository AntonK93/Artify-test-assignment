import { Model } from '@vuex-orm/core';

export class Sector extends Model {
    // This is the name used as module name of the Vuex Store.
    static entity = 'sectors';

    static fields() {
        return {
            id: this.attr(null),
            name: this.attr(null),
            parent: this.attr(null),
            children: this.attr(null),
        };
    }
}

export default Sector;

// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

// Export members:
export { GetItemArgs, GetItemResult, GetItemOutputArgs } from "./getItem";
export const getItem: typeof import("./getItem").getItem = null as any;
export const getItemOutput: typeof import("./getItem").getItemOutput = null as any;
utilities.lazyLoad(exports, ["getItem","getItemOutput"], () => require("./getItem"));

export { GetVaultArgs, GetVaultResult, GetVaultOutputArgs } from "./getVault";
export const getVault: typeof import("./getVault").getVault = null as any;
export const getVaultOutput: typeof import("./getVault").getVaultOutput = null as any;
utilities.lazyLoad(exports, ["getVault","getVaultOutput"], () => require("./getVault"));

export { ItemArgs, ItemState } from "./item";
export type Item = import("./item").Item;
export const Item: typeof import("./item").Item = null as any;
utilities.lazyLoad(exports, ["Item"], () => require("./item"));

export { ProviderArgs } from "./provider";
export type Provider = import("./provider").Provider;
export const Provider: typeof import("./provider").Provider = null as any;
utilities.lazyLoad(exports, ["Provider"], () => require("./provider"));


// Export sub-modules:
import * as config from "./config";
import * as types from "./types";

export {
    config,
    types,
};

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "onepassword:index/item:Item":
                return new Item(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("onepassword", "index/item", _module)
pulumi.runtime.registerResourcePackage("onepassword", {
    version: utilities.getVersion(),
    constructProvider: (name: string, type: string, urn: string): pulumi.ProviderResource => {
        if (type !== "pulumi:providers:onepassword") {
            throw new Error(`unknown provider type ${type}`);
        }
        return new Provider(name, <any>undefined, { urn });
    },
});

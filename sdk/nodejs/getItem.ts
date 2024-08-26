// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

export function getItem(args: GetItemArgs, opts?: pulumi.InvokeOptions): Promise<GetItemResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("onepassword:index/getItem:getItem", {
        "files": args.files,
        "noteValue": args.noteValue,
        "sections": args.sections,
        "title": args.title,
        "uuid": args.uuid,
        "vault": args.vault,
    }, opts);
}

/**
 * A collection of arguments for invoking getItem.
 */
export interface GetItemArgs {
    files?: inputs.GetItemFile[];
    noteValue?: string;
    sections?: inputs.GetItemSection[];
    title?: string;
    uuid?: string;
    vault: string;
}

/**
 * A collection of values returned by getItem.
 */
export interface GetItemResult {
    readonly category: string;
    readonly credential: string;
    readonly database: string;
    readonly files?: outputs.GetItemFile[];
    readonly hostname: string;
    readonly id: string;
    readonly noteValue: string;
    readonly password: string;
    readonly port: string;
    readonly privateKey: string;
    readonly publicKey: string;
    readonly sections?: outputs.GetItemSection[];
    readonly tags: string[];
    readonly title: string;
    readonly type: string;
    readonly url: string;
    readonly username: string;
    readonly uuid: string;
    readonly vault: string;
}
export function getItemOutput(args: GetItemOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetItemResult> {
    return pulumi.output(args).apply((a: any) => getItem(a, opts))
}

/**
 * A collection of arguments for invoking getItem.
 */
export interface GetItemOutputArgs {
    files?: pulumi.Input<pulumi.Input<inputs.GetItemFileArgs>[]>;
    noteValue?: pulumi.Input<string>;
    sections?: pulumi.Input<pulumi.Input<inputs.GetItemSectionArgs>[]>;
    title?: pulumi.Input<string>;
    uuid?: pulumi.Input<string>;
    vault: pulumi.Input<string>;
}

// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Onepassword.Inputs
{

    public sealed class ItemSectionArgs : global::Pulumi.ResourceArgs
    {
        [Input("fields")]
        private InputList<Inputs.ItemSectionFieldArgs>? _fields;

        /// <summary>
        /// A list of custom fields in the section.
        /// </summary>
        public InputList<Inputs.ItemSectionFieldArgs> Fields
        {
            get => _fields ?? (_fields = new InputList<Inputs.ItemSectionFieldArgs>());
            set => _fields = value;
        }

        /// <summary>
        /// A unique identifier for the section.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// The label for the section.
        /// </summary>
        [Input("label", required: true)]
        public Input<string> Label { get; set; } = null!;

        public ItemSectionArgs()
        {
        }
        public static new ItemSectionArgs Empty => new ItemSectionArgs();
    }
}

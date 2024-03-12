// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Onepassword.Outputs
{

    [OutputType]
    public sealed class GetItemSectionResult
    {
        /// <summary>
        /// A list of custom fields in the section.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetItemSectionFieldResult> Fields;
        /// <summary>
        /// A unique identifier for the section.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// The label for the section.
        /// </summary>
        public readonly string Label;

        [OutputConstructor]
        private GetItemSectionResult(
            ImmutableArray<Outputs.GetItemSectionFieldResult> fields,

            string id,

            string label)
        {
            Fields = fields;
            Id = id;
            Label = label;
        }
    }
}

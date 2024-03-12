// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Onepassword.Inputs
{

    public sealed class ItemSectionFieldGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// A unique identifier for the field.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// The label for the field.
        /// </summary>
        [Input("label", required: true)]
        public Input<string> Label { get; set; } = null!;

        /// <summary>
        /// Password for this item.
        /// </summary>
        [Input("passwordRecipe")]
        public Input<Inputs.ItemSectionFieldPasswordRecipeGetArgs>? PasswordRecipe { get; set; }

        /// <summary>
        /// Purpose indicates this is a special field: a username, password, or notes field. One of ["USERNAME" "PASSWORD" "NOTES"]
        /// </summary>
        [Input("purpose")]
        public Input<string>? Purpose { get; set; }

        /// <summary>
        /// The type of value stored in the field. One of ["STRING" "EMAIL" "CONCEALED" "URL" "OTP" "DATE" "MONTH_YEAR" "MENU"]
        /// </summary>
        [Input("type")]
        public Input<string>? Type { get; set; }

        [Input("value")]
        private Input<string>? _value;

        /// <summary>
        /// The value of the field.
        /// </summary>
        public Input<string>? Value
        {
            get => _value;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _value = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        public ItemSectionFieldGetArgs()
        {
        }
        public static new ItemSectionFieldGetArgs Empty => new ItemSectionFieldGetArgs();
    }
}

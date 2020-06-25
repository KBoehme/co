// <auto-generated />
//
// To parse this JSON data, add NuGet 'Newtonsoft.Json' then do one of these:
//
//    using QuickType;
//
//    var fastQ = FastQ.FromJson(jsonString);
//    var bam = Bam.FromJson(jsonString);
//    var vcf = Vcf.FromJson(jsonString);
//    var bed = Bed.FromJson(jsonString);
//    var variant = Variant.FromJson(jsonString);

namespace QuickType
{
    using System;
    using System.Collections.Generic;

    using System.Globalization;
    using Newtonsoft.Json;
    using Newtonsoft.Json.Converters;

    public partial class FastQ
    {
        [JsonProperty("path")]
        public string Path { get; set; }
    }

    public partial class Bam
    {
        [JsonProperty("path")]
        public string Path { get; set; }
    }

    public partial class Vcf
    {
        [JsonProperty("path")]
        public string Path { get; set; }
    }

    public partial class Bed
    {
        [JsonProperty("path")]
        public string Path { get; set; }
    }

    public partial class Variant
    {
        [JsonProperty("path")]
        public string Path { get; set; }
    }

    public partial class FastQ
    {
        public static FastQ FromJson(string json) => JsonConvert.DeserializeObject<FastQ>(json, QuickType.Converter.Settings);
    }

    public partial class Bam
    {
        public static Bam FromJson(string json) => JsonConvert.DeserializeObject<Bam>(json, QuickType.Converter.Settings);
    }

    public partial class Vcf
    {
        public static Vcf FromJson(string json) => JsonConvert.DeserializeObject<Vcf>(json, QuickType.Converter.Settings);
    }

    public partial class Bed
    {
        public static Bed FromJson(string json) => JsonConvert.DeserializeObject<Bed>(json, QuickType.Converter.Settings);
    }

    public partial class Variant
    {
        public static Variant FromJson(string json) => JsonConvert.DeserializeObject<Variant>(json, QuickType.Converter.Settings);
    }

    public static class Serialize
    {
        public static string ToJson(this FastQ self) => JsonConvert.SerializeObject(self, QuickType.Converter.Settings);
        public static string ToJson(this Bam self) => JsonConvert.SerializeObject(self, QuickType.Converter.Settings);
        public static string ToJson(this Vcf self) => JsonConvert.SerializeObject(self, QuickType.Converter.Settings);
        public static string ToJson(this Bed self) => JsonConvert.SerializeObject(self, QuickType.Converter.Settings);
        public static string ToJson(this Variant self) => JsonConvert.SerializeObject(self, QuickType.Converter.Settings);
    }

    internal static class Converter
    {
        public static readonly JsonSerializerSettings Settings = new JsonSerializerSettings
        {
            MetadataPropertyHandling = MetadataPropertyHandling.Ignore,
            DateParseHandling = DateParseHandling.None,
            Converters =
            {
                new IsoDateTimeConverter { DateTimeStyles = DateTimeStyles.AssumeUniversal }
            },
        };
    }
}
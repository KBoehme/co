// To use this code, add the following Maven dependency to your project:
//
//
//     com.fasterxml.jackson.core : jackson-databind : 2.9.0
//
// Import this package:
//
//     import io.quicktype.Converter;
//
// Then you can deserialize a JSON string with
//
//     FastQ data = Converter.FastQFromJsonString(jsonString);
//     BAM data = Converter.BAMFromJsonString(jsonString);
//     Vcf data = Converter.VcfFromJsonString(jsonString);
//     Bed data = Converter.BedFromJsonString(jsonString);
//     Variant data = Converter.VariantFromJsonString(jsonString);

package io.quicktype;

import java.util.*;
import java.io.IOException;
import com.fasterxml.jackson.databind.*;
import com.fasterxml.jackson.core.JsonProcessingException;

public class Converter {
    // Serialize/deserialize helpers

    public static FastQ FastQFromJsonString(String json) throws IOException {
        return getFastQObjectReader().readValue(json);
    }

    public static String FastQToJsonString(FastQ obj) throws JsonProcessingException {
        return getFastQObjectWriter().writeValueAsString(obj);
    }

    public static BAM BAMFromJsonString(String json) throws IOException {
        return getBAMObjectReader().readValue(json);
    }

    public static String BAMToJsonString(BAM obj) throws JsonProcessingException {
        return getBAMObjectWriter().writeValueAsString(obj);
    }

    public static Vcf VcfFromJsonString(String json) throws IOException {
        return getVcfObjectReader().readValue(json);
    }

    public static String VcfToJsonString(Vcf obj) throws JsonProcessingException {
        return getVcfObjectWriter().writeValueAsString(obj);
    }

    public static Bed BedFromJsonString(String json) throws IOException {
        return getBedObjectReader().readValue(json);
    }

    public static String BedToJsonString(Bed obj) throws JsonProcessingException {
        return getBedObjectWriter().writeValueAsString(obj);
    }

    public static Variant VariantFromJsonString(String json) throws IOException {
        return getVariantObjectReader().readValue(json);
    }

    public static String VariantToJsonString(Variant obj) throws JsonProcessingException {
        return getVariantObjectWriter().writeValueAsString(obj);
    }

    private static ObjectReader FastQReader;
    private static ObjectWriter FastQWriter;

    private static void instantiateFastQMapper() {
        ObjectMapper mapper = new ObjectMapper();
        FastQReader = mapper.readerFor(FastQ.class);
        FastQWriter = mapper.writerFor(FastQ.class);
    }

    private static ObjectReader getFastQObjectReader() {
        if (FastQReader == null) instantiateFastQMapper();
        return FastQReader;
    }

    private static ObjectWriter getFastQObjectWriter() {
        if (FastQWriter == null) instantiateFastQMapper();
        return FastQWriter;
    }

    private static ObjectReader BAMReader;
    private static ObjectWriter BAMWriter;

    private static void instantiateBAMMapper() {
        ObjectMapper mapper = new ObjectMapper();
        BAMReader = mapper.readerFor(BAM.class);
        BAMWriter = mapper.writerFor(BAM.class);
    }

    private static ObjectReader getBAMObjectReader() {
        if (BAMReader == null) instantiateBAMMapper();
        return BAMReader;
    }

    private static ObjectWriter getBAMObjectWriter() {
        if (BAMWriter == null) instantiateBAMMapper();
        return BAMWriter;
    }

    private static ObjectReader VcfReader;
    private static ObjectWriter VcfWriter;

    private static void instantiateVcfMapper() {
        ObjectMapper mapper = new ObjectMapper();
        VcfReader = mapper.readerFor(Vcf.class);
        VcfWriter = mapper.writerFor(Vcf.class);
    }

    private static ObjectReader getVcfObjectReader() {
        if (VcfReader == null) instantiateVcfMapper();
        return VcfReader;
    }

    private static ObjectWriter getVcfObjectWriter() {
        if (VcfWriter == null) instantiateVcfMapper();
        return VcfWriter;
    }

    private static ObjectReader BedReader;
    private static ObjectWriter BedWriter;

    private static void instantiateBedMapper() {
        ObjectMapper mapper = new ObjectMapper();
        BedReader = mapper.readerFor(Bed.class);
        BedWriter = mapper.writerFor(Bed.class);
    }

    private static ObjectReader getBedObjectReader() {
        if (BedReader == null) instantiateBedMapper();
        return BedReader;
    }

    private static ObjectWriter getBedObjectWriter() {
        if (BedWriter == null) instantiateBedMapper();
        return BedWriter;
    }

    private static ObjectReader VariantReader;
    private static ObjectWriter VariantWriter;

    private static void instantiateVariantMapper() {
        ObjectMapper mapper = new ObjectMapper();
        VariantReader = mapper.readerFor(Variant.class);
        VariantWriter = mapper.writerFor(Variant.class);
    }

    private static ObjectReader getVariantObjectReader() {
        if (VariantReader == null) instantiateVariantMapper();
        return VariantReader;
    }

    private static ObjectWriter getVariantObjectWriter() {
        if (VariantWriter == null) instantiateVariantMapper();
        return VariantWriter;
    }
}

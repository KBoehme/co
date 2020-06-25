// This file was generated from JSON Schema using quicktype, do not modify it directly.
// To parse and unparse this JSON data, add this code to your project and do:
//
//    fastQ, err := UnmarshalFastQ(bytes)
//    bytes, err = fastQ.Marshal()
//
//    bAM, err := UnmarshalBAM(bytes)
//    bytes, err = bAM.Marshal()
//
//    vcf, err := UnmarshalVcf(bytes)
//    bytes, err = vcf.Marshal()
//
//    bed, err := UnmarshalBed(bytes)
//    bytes, err = bed.Marshal()
//
//    variant, err := UnmarshalVariant(bytes)
//    bytes, err = variant.Marshal()

package main

import "encoding/json"

func UnmarshalFastQ(data []byte) (FastQ, error) {
	var r FastQ
	err := json.Unmarshal(data, &r)
	return r, err
}

func (r *FastQ) Marshal() ([]byte, error) {
	return json.Marshal(r)
}

func UnmarshalBAM(data []byte) (BAM, error) {
	var r BAM
	err := json.Unmarshal(data, &r)
	return r, err
}

func (r *BAM) Marshal() ([]byte, error) {
	return json.Marshal(r)
}

func UnmarshalVcf(data []byte) (Vcf, error) {
	var r Vcf
	err := json.Unmarshal(data, &r)
	return r, err
}

func (r *Vcf) Marshal() ([]byte, error) {
	return json.Marshal(r)
}

func UnmarshalBed(data []byte) (Bed, error) {
	var r Bed
	err := json.Unmarshal(data, &r)
	return r, err
}

func (r *Bed) Marshal() ([]byte, error) {
	return json.Marshal(r)
}

func UnmarshalVariant(data []byte) (Variant, error) {
	var r Variant
	err := json.Unmarshal(data, &r)
	return r, err
}

func (r *Variant) Marshal() ([]byte, error) {
	return json.Marshal(r)
}

type FastQ struct {
	Path string `json:"path"`
}

type BAM struct {
	Path string `json:"path"`
}

type Vcf struct {
	Path string `json:"path"`
}

type Bed struct {
	Path string `json:"path"`
}

type Variant struct {
	Path string `json:"path"`
}

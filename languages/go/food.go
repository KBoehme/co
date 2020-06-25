// This file was generated from JSON Schema using quicktype, do not modify it directly.
// To parse and unparse this JSON data, add this code to your project and do:
//
//    pantry, err := UnmarshalPantry(bytes)
//    bytes, err = pantry.Marshal()
//
//    fridge, err := UnmarshalFridge(bytes)
//    bytes, err = fridge.Marshal()
//
//    breadSlice, err := UnmarshalBreadSlice(bytes)
//    bytes, err = breadSlice.Marshal()
//
//    jelly, err := UnmarshalJelly(bytes)
//    bytes, err = jelly.Marshal()
//
//    pb, err := UnmarshalPb(bytes)
//    bytes, err = pb.Marshal()
//
//    jellySlice, err := UnmarshalJellySlice(bytes)
//    bytes, err = jellySlice.Marshal()
//
//    pBSlice, err := UnmarshalPBSlice(bytes)
//    bytes, err = pBSlice.Marshal()
//
//    pBJSandwhich, err := UnmarshalPBJSandwhich(bytes)
//    bytes, err = pBJSandwhich.Marshal()

package main

import "encoding/json"

func UnmarshalPantry(data []byte) (Pantry, error) {
	var r Pantry
	err := json.Unmarshal(data, &r)
	return r, err
}

func (r *Pantry) Marshal() ([]byte, error) {
	return json.Marshal(r)
}

func UnmarshalFridge(data []byte) (Fridge, error) {
	var r Fridge
	err := json.Unmarshal(data, &r)
	return r, err
}

func (r *Fridge) Marshal() ([]byte, error) {
	return json.Marshal(r)
}

func UnmarshalBreadSlice(data []byte) (BreadSlice, error) {
	var r BreadSlice
	err := json.Unmarshal(data, &r)
	return r, err
}

func (r *BreadSlice) Marshal() ([]byte, error) {
	return json.Marshal(r)
}

func UnmarshalJelly(data []byte) (Jelly, error) {
	var r Jelly
	err := json.Unmarshal(data, &r)
	return r, err
}

func (r *Jelly) Marshal() ([]byte, error) {
	return json.Marshal(r)
}

func UnmarshalPb(data []byte) (Pb, error) {
	var r Pb
	err := json.Unmarshal(data, &r)
	return r, err
}

func (r *Pb) Marshal() ([]byte, error) {
	return json.Marshal(r)
}

func UnmarshalJellySlice(data []byte) (JellySlice, error) {
	var r JellySlice
	err := json.Unmarshal(data, &r)
	return r, err
}

func (r *JellySlice) Marshal() ([]byte, error) {
	return json.Marshal(r)
}

func UnmarshalPBSlice(data []byte) (PBSlice, error) {
	var r PBSlice
	err := json.Unmarshal(data, &r)
	return r, err
}

func (r *PBSlice) Marshal() ([]byte, error) {
	return json.Marshal(r)
}

func UnmarshalPBJSandwhich(data []byte) (PBJSandwhich, error) {
	var r PBJSandwhich
	err := json.Unmarshal(data, &r)
	return r, err
}

func (r *PBJSandwhich) Marshal() ([]byte, error) {
	return json.Marshal(r)
}

type Pantry struct {
	Path string `json:"path"`
}

type Fridge struct {
	Path string `json:"path"`
}

type BreadSlice struct {
	Path string `json:"path"`
}

type Jelly struct {
	Path string `json:"path"`
}

type Pb struct {
	Path string `json:"path"`
}

type JellySlice struct {
	Path string `json:"path"`
}

type PBSlice struct {
	Path string `json:"path"`
}

type PBJSandwhich struct {
	Path string `json:"path"`
}

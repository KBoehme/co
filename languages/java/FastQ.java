package io.quicktype;

import java.util.*;
import com.fasterxml.jackson.annotation.*;

public class FastQ {
    private String path;

    @JsonProperty("path")
    public String getPath() { return path; }
    @JsonProperty("path")
    public void setPath(String value) { this.path = value; }
}

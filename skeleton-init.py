#!/usr/bin/env python2
import sys, os, shutil

project = sys.argv[1]

class_skeleton = """/**
 * @author Jacob Salzberg
 */
public class {} {{
    /**
     * @param args Command line arguments. Not used.
     */
    public static void main(String[] args) {{
        System.out.println("Hello world!");
    }}
}}
"""


class_generated = class_skeleton.format(project)

test_skeleton = """import static org.junit.Assert.*;
import org.junit.Test;
/**
  * @author Jacob Salzberg
  */
public class {} {{
    /**
      *
      */
      @Test
      public void test() {{
      }}
}}
"""

test_generated = test_skeleton.format(project)

class_filename = project + ".java"

test_filename = project + "Test.java"

def withd(pushdir, k):
    currdir = os.getcwd()
    os.chdir(pushdir)
    k()
    os.chdir(currdir)

def write(s, name):
    f = open(name, "w")
    f.write(class_generated)
    f.close()

if not os.path.exists(project):
    shutil.copytree('skeleton', project)
    os.chdir(project)
    for dir in ["src", "test", "project_docs", "bin"]:
        os.makedirs(dir)
    
    withd("src", lambda: write(class_generated, class_filename))
    withd("test", lambda: write(test_generated, test_filename))
else:
    print("Project {} already exists".format(project))

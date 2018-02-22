#!/usr/bin/env python2
import sys, os, shutil

toplevel = os.path.dirname(os.path.realpath(__file__))

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

def write(s, name):
    f = open(name, "w")
    f.write(class_generated)
    f.close()

if not os.path.exists(project):
    shutil.copytree('{}/skeleton'.format(toplevel), project)
    os.chdir(project)
    for dir in ["src", "test", "project_docs", "bin"]:
        if not os.path.exists(dir):
            os.makedirs(dir)
    
    f = open("src/{}".format(class_filename), "w")
    f.write(class_generated)
    f.close()

    f = open("test/{}".format(test_filename), "w")
    f.write(test_generated)
    f.close()
else:
    print("Project {} already exists".format(project))

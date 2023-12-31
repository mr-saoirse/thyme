# thyme: talking in types

This is an experimental type only library. How an LLM can be used to build a library of validating types with Pydantic. The AI is used to make all edits.

This is a completely isolated repo. We break some rules because we assume that AI automation can be used to modify the repo and push changes to Git at will.
This is not completely realistic today and that is why its a stand alone repo. In the limit however, we can manage certain functions completely autonomously. This repos explores which.

An example workflow

```python
#this will build all the types in the namespace "one" from the diagram and doc string in init.py
poetry run thyme ns build -p one
#git context
#get the changes locally or from remote
poetry run thyme git changes --remote  
#push the changes with git cli, auto merge the branch to main
poetry run thyme git push
#if you want to not auto merge and review the changes...
poetry run thyme git push --review

#we can also rebase the main branch at any time
poetry run thyme git rebase

```

The flow is as follows

- We draw a diagram in each namespace for the types
- We get all the types that are there and we ask the LLM to generate a set of class files for each diagram
- the root validator by convention also calls out to a dummy root validator for each type that the developer can override
- we inherit from a common base for the namespace which can be changed per namespace
- namespaces are small enough that we can be modular and compact e.g. 5-10 types at most per namespace
- We take hints from reference types
- We can describe validations in "about" classes which are added to docstrings of the type. the init.py carries descriptions for the namespace
- we write tests to make sure that the types are correct and validation is correct (later we add tests in our git actions build)
- We ask the agent to create ops in the ops library -they are always documented properly with doc strings and can be "indexed"
- Indexed ops can be used by the agent too if needed to solve other tasks

This means that the role of the developer is elevated/demoted to design and testing only and we are only allow write code by asking the LLM to do it, one way or another.

## Special fields for interfaces - teaching the LLM more semantics

- describes how we would save it e.g. numeric, large text etc. This is semantic information that the LLM knows that a code thing would not normally know but we can use for control
- relationships to other types
- validators

# Design/Flow

- describe what you are doing as a diagram
- take my diagram and generate some code to glue
- use init.py doc strings to add extra context
- write unit tests to guide the LLM and also check the code works
- Commit the code to git, tests runs and merges to main with docker built
-

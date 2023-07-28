import ruamel.yaml
import os
from abc import abstractmethod

# the latest tag is: the latest language version + the latest os version, usually the last indices

###############################
#           Versions          #
###############################
golang_versions      = ["1.19.10", ]
node_versions        = ["16.17.1-nslt", ]
python_versions      = ["3.8", "3.11.1", ]
tensorflow_versions  = ["1.15.5", ]

os__versions      = {
    "anolis":       ["8.6", "8.8"],
    "alinux":       ["3"],
}

###############################
#           Generator         #
###############################

TYPE       = "configs"
IMAGES     = "images"
FOLDER     = "folder"
DOCKERFILE = "dockerfile"
BUILDS     = "builds"
ARGS       = "args"
TAGS       = "tags"
REGISTRIES = "registries"

# Abstract
class LanguageContainer:
    def __init__(self):
        pass

    @abstractmethod
    def folder(self):
        pass

    @abstractmethod
    def versions(self):
        pass

    def tagPatterns(self):
        return [
            "{VERSION}-{OS_VERSION}",  # e.g. 1.19.5-8.6
        ]

    def dockerfiles(self):
        return ["Dockerfile"]

    def os_versions(self):
        return os__versions

    def registries(self):
        return {
            "anolis": "anolis",
            "alinux": "alinux"
        }

    def generateDockerImageConfigs(self):
        pass


# Golang definitions
class Golang(LanguageContainer):
    def folder(self):
        return "golang"

    def versions(self):
        return golang_versions


# Python definitions
class Python(LanguageContainer):
    def folder(self):
        return "python"

    def versions(self):
        return python_versions


# Node definitions
class Node(LanguageContainer):
    def folder(self):
        return "node"

    def versions(self):
        return node_versions


# Tensorflow definitions
class Tensorflow(LanguageContainer):
    def folder(self):
        return "tensorflow"

    def versions(self):
        return tensorflow_versions


class NoAliasDumper(ruamel.yaml.representer.RoundTripRepresenter):
    def ignore_aliases(self, data):
        return True


class ConfigGenerator:
    def __init__(self, language):
        self.language = language

    def generateObject(self):
        lang = self.language
        object = {
            lang.folder(): {}                        # e.g. golang
        }
        for version_idx in range(len(lang.versions())):
            version = lang.versions()[version_idx]   # e.g. 1.9.5
            object[lang.folder()][version] = {}
            for os_name in lang.os_versions():       # e.g. anolis/alinux
                images = []
                object[lang.folder()][version][os_name] = {
                    REGISTRIES: [lang.registries()[os_name]],
                    IMAGES:     images
                }
                for os_version_idx in range(len(lang.os_versions()[os_name])):
                    os_version = lang.os_versions()[os_name][os_version_idx]             # e.g. 8.6 (for anolis)
                    folder = os.path.join(lang.folder(), version, os_name + os_version)  # e.g. golang/1.9.5/anolis8.6
                    for dockerfile in lang.dockerfiles():                                # e.g. Dockerfile
                        # fill dockerfile info
                        dockerfile_path = os.path.join(folder, dockerfile)
                        assert os.path.exists(os.path.join(os.path.dirname(os.path.realpath(__file__)), dockerfile_path))
                        dockerfile_object = {
                            DOCKERFILE: dockerfile_path,
                            BUILDS: []
                        }
                        images.append(dockerfile_object)
                        # fill tag info
                        tags = []
                        for tag_pattern in lang.tagPatterns():
                            tags.append(tag_pattern.format(VERSION=version,
                                                           OS_VERSION=os_version))
                        # the latest tag
                        if version_idx == len(lang.versions())-1 and os_version_idx == len(lang.os_versions()[os_name])-1:
                            tags.append("latest")

                        # append tags
                        dockerfile_object[BUILDS].append({
                            TAGS: tags
                        })
        return object

    def generate(self):
        object = self.generateObject()
        file_pwd = os.path.dirname(os.path.realpath(__file__))
        # dump YAML
        with open(os.path.join(file_pwd, self.language.folder(), 'versions.yaml'), 'w') as f:
            yml = ruamel.yaml.YAML()
            yml.preserve_quotes = False
            yml.Representer = NoAliasDumper
            yml.dump(object, f)


ConfigGenerator(Golang()).generate()
ConfigGenerator(Python()).generate()
ConfigGenerator(Node()).generate()
ConfigGenerator(Tensorflow()).generate()

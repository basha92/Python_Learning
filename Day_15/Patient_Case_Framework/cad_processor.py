#this file handles tibial, femoral and insert parts.

class CADProcessor:

    def process_parts(self, parts):

        results = []

        for part in parts:

            try:
                results.append(part.validate())
                results.append(part.process())
                results.append(part.export())

            except ValueError as error:
                results.append(
                    f"Part {part.part_number} failed: {error}"
                )

        return results
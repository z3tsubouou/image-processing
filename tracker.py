# TechVidvan Vehicle-Tracker

import math

class EuclideanDistTracker:
    def __init__(self):
        #objectiin goliin bairlaliig hadgalah")
        self.center_points = {}
        #shine too object tanigdah bolgond nemej toog hadgalah")
        self.id_count = 0


    def update(self, objects_rect):
        #objectiin id tai hadgalah")
        objects_bbs_ids = []

        #shine objectiin gol tsegiig oloh")
        for rect in objects_rect:
            x, y, w, h, index = rect
            cx = (x + x + w) // 2
            cy = (y + y + h) // 2

            #ali hediin oldson object baina uu gedgiig shalgah")
            same_object_detected = False
            for id, pt in self.center_points.items():
                dist = math.hypot(cx - pt[0], cy - pt[1])

                if dist < 25:
                    self.center_points[id] = (cx, cy)
                    objects_bbs_ids.append([x, y, w, h, id, index])
                    same_object_detected = True
                    break

            #shine object tanigdah yum bol shineer hadgalj uguh")
            if same_object_detected is False:
                self.center_points[self.id_count] = (cx, cy)
                objects_bbs_ids.append([x, y, w, h, self.id_count, index])
                self.id_count += 1

        #ashiglagdahaa bolison objectiig id-g ustgah")
        new_center_points = {}
        for obj_bb_id in objects_bbs_ids:
            _, _, _, _, object_id, index = obj_bb_id
            center = self.center_points[object_id]
            new_center_points[object_id] = center

        #dictionary utgiig ashiglagdahaa bolison utgiig hasaj shinechleh")
        self.center_points = new_center_points.copy()
        return objects_bbs_ids



def ad(a, b):
    return a+b
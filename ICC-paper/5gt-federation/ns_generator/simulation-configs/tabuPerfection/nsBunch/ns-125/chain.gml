graph [
  node [
    id 0
    label 1
    disk 8
    cpu 2
    memory 5
  ]
  node [
    id 1
    label 2
    disk 1
    cpu 4
    memory 6
  ]
  node [
    id 2
    label 3
    disk 6
    cpu 2
    memory 10
  ]
  node [
    id 3
    label 4
    disk 8
    cpu 3
    memory 16
  ]
  node [
    id 4
    label 5
    disk 8
    cpu 2
    memory 5
  ]
  node [
    id 5
    label 6
    disk 4
    cpu 2
    memory 16
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 25
    bw 179
  ]
  edge [
    source 0
    target 1
    delay 28
    bw 159
  ]
  edge [
    source 0
    target 2
    delay 26
    bw 153
  ]
  edge [
    source 1
    target 4
    delay 30
    bw 57
  ]
  edge [
    source 2
    target 3
    delay 33
    bw 53
  ]
  edge [
    source 3
    target 4
    delay 30
    bw 198
  ]
  edge [
    source 4
    target 5
    delay 35
    bw 158
  ]
]

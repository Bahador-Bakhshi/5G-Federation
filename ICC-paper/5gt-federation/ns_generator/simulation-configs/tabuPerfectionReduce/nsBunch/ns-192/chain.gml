graph [
  node [
    id 0
    label 1
    disk 5
    cpu 4
    memory 15
  ]
  node [
    id 1
    label 2
    disk 1
    cpu 2
    memory 3
  ]
  node [
    id 2
    label 3
    disk 4
    cpu 4
    memory 16
  ]
  node [
    id 3
    label 4
    disk 1
    cpu 2
    memory 11
  ]
  node [
    id 4
    label 5
    disk 1
    cpu 1
    memory 8
  ]
  node [
    id 5
    label 6
    disk 5
    cpu 1
    memory 4
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 31
    bw 115
  ]
  edge [
    source 0
    target 1
    delay 27
    bw 80
  ]
  edge [
    source 0
    target 2
    delay 26
    bw 53
  ]
  edge [
    source 0
    target 3
    delay 34
    bw 146
  ]
  edge [
    source 1
    target 4
    delay 28
    bw 68
  ]
  edge [
    source 2
    target 5
    delay 30
    bw 96
  ]
  edge [
    source 3
    target 5
    delay 33
    bw 146
  ]
  edge [
    source 4
    target 5
    delay 26
    bw 78
  ]
]

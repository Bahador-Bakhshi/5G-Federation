graph [
  node [
    id 0
    label 1
    disk 8
    cpu 3
    memory 6
  ]
  node [
    id 1
    label 2
    disk 7
    cpu 1
    memory 8
  ]
  node [
    id 2
    label 3
    disk 3
    cpu 4
    memory 8
  ]
  node [
    id 3
    label 4
    disk 7
    cpu 3
    memory 1
  ]
  node [
    id 4
    label 5
    disk 10
    cpu 2
    memory 6
  ]
  node [
    id 5
    label 6
    disk 1
    cpu 1
    memory 11
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 33
    bw 151
  ]
  edge [
    source 0
    target 1
    delay 29
    bw 118
  ]
  edge [
    source 0
    target 2
    delay 30
    bw 75
  ]
  edge [
    source 0
    target 3
    delay 28
    bw 95
  ]
  edge [
    source 1
    target 4
    delay 25
    bw 72
  ]
  edge [
    source 2
    target 5
    delay 30
    bw 94
  ]
  edge [
    source 3
    target 5
    delay 33
    bw 54
  ]
  edge [
    source 4
    target 5
    delay 26
    bw 193
  ]
]

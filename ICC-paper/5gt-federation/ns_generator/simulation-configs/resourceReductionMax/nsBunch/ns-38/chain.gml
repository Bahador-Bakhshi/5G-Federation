graph [
  node [
    id 0
    label 1
    disk 9
    cpu 4
    memory 8
  ]
  node [
    id 1
    label 2
    disk 2
    cpu 2
    memory 16
  ]
  node [
    id 2
    label 3
    disk 9
    cpu 2
    memory 5
  ]
  node [
    id 3
    label 4
    disk 6
    cpu 1
    memory 4
  ]
  node [
    id 4
    label 5
    disk 4
    cpu 3
    memory 3
  ]
  node [
    id 5
    label 6
    disk 7
    cpu 3
    memory 14
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 28
    bw 167
  ]
  edge [
    source 0
    target 1
    delay 31
    bw 82
  ]
  edge [
    source 0
    target 2
    delay 28
    bw 133
  ]
  edge [
    source 0
    target 3
    delay 35
    bw 119
  ]
  edge [
    source 1
    target 4
    delay 28
    bw 92
  ]
  edge [
    source 2
    target 4
    delay 26
    bw 61
  ]
  edge [
    source 3
    target 5
    delay 27
    bw 104
  ]
  edge [
    source 4
    target 5
    delay 27
    bw 135
  ]
]

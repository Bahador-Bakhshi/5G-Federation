graph [
  node [
    id 0
    label 1
    disk 9
    cpu 4
    memory 12
  ]
  node [
    id 1
    label 2
    disk 6
    cpu 1
    memory 3
  ]
  node [
    id 2
    label 3
    disk 2
    cpu 3
    memory 4
  ]
  node [
    id 3
    label 4
    disk 4
    cpu 3
    memory 3
  ]
  node [
    id 4
    label 5
    disk 1
    cpu 4
    memory 3
  ]
  node [
    id 5
    label 6
    disk 6
    cpu 2
    memory 2
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 31
    bw 116
  ]
  edge [
    source 0
    target 1
    delay 31
    bw 81
  ]
  edge [
    source 0
    target 2
    delay 35
    bw 188
  ]
  edge [
    source 0
    target 3
    delay 27
    bw 163
  ]
  edge [
    source 1
    target 4
    delay 30
    bw 135
  ]
  edge [
    source 2
    target 4
    delay 35
    bw 68
  ]
  edge [
    source 3
    target 4
    delay 33
    bw 196
  ]
  edge [
    source 4
    target 5
    delay 32
    bw 135
  ]
]

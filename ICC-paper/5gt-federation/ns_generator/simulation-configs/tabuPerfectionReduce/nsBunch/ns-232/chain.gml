graph [
  node [
    id 0
    label 1
    disk 6
    cpu 2
    memory 3
  ]
  node [
    id 1
    label 2
    disk 5
    cpu 3
    memory 5
  ]
  node [
    id 2
    label 3
    disk 2
    cpu 2
    memory 12
  ]
  node [
    id 3
    label 4
    disk 1
    cpu 4
    memory 12
  ]
  node [
    id 4
    label 5
    disk 9
    cpu 4
    memory 14
  ]
  node [
    id 5
    label 6
    disk 9
    cpu 4
    memory 16
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 32
    bw 78
  ]
  edge [
    source 0
    target 1
    delay 26
    bw 163
  ]
  edge [
    source 1
    target 2
    delay 26
    bw 82
  ]
  edge [
    source 2
    target 3
    delay 29
    bw 181
  ]
  edge [
    source 3
    target 4
    delay 33
    bw 108
  ]
  edge [
    source 3
    target 5
    delay 30
    bw 69
  ]
]

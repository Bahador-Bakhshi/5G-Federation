graph [
  node [
    id 0
    label 1
    disk 5
    cpu 2
    memory 16
  ]
  node [
    id 1
    label 2
    disk 6
    cpu 2
    memory 14
  ]
  node [
    id 2
    label 3
    disk 8
    cpu 1
    memory 4
  ]
  node [
    id 3
    label 4
    disk 10
    cpu 2
    memory 16
  ]
  node [
    id 4
    label 5
    disk 1
    cpu 4
    memory 9
  ]
  node [
    id 5
    label 6
    disk 8
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
    delay 26
    bw 188
  ]
  edge [
    source 0
    target 1
    delay 26
    bw 109
  ]
  edge [
    source 1
    target 2
    delay 27
    bw 196
  ]
  edge [
    source 2
    target 3
    delay 25
    bw 190
  ]
  edge [
    source 3
    target 4
    delay 31
    bw 89
  ]
  edge [
    source 4
    target 5
    delay 25
    bw 116
  ]
]

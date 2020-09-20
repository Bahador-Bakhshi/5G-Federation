graph [
  node [
    id 0
    label 1
    disk 3
    cpu 3
    memory 3
  ]
  node [
    id 1
    label 2
    disk 2
    cpu 3
    memory 8
  ]
  node [
    id 2
    label 3
    disk 1
    cpu 1
    memory 2
  ]
  node [
    id 3
    label 4
    disk 2
    cpu 3
    memory 16
  ]
  node [
    id 4
    label 5
    disk 6
    cpu 1
    memory 10
  ]
  node [
    id 5
    label 6
    disk 5
    cpu 3
    memory 8
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 35
    bw 159
  ]
  edge [
    source 0
    target 1
    delay 27
    bw 153
  ]
  edge [
    source 1
    target 2
    delay 32
    bw 97
  ]
  edge [
    source 1
    target 3
    delay 27
    bw 106
  ]
  edge [
    source 1
    target 4
    delay 28
    bw 151
  ]
  edge [
    source 3
    target 5
    delay 28
    bw 154
  ]
]

graph [
  node [
    id 0
    label 1
    disk 6
    cpu 1
    memory 7
  ]
  node [
    id 1
    label 2
    disk 1
    cpu 4
    memory 16
  ]
  node [
    id 2
    label 3
    disk 4
    cpu 3
    memory 6
  ]
  node [
    id 3
    label 4
    disk 7
    cpu 4
    memory 8
  ]
  node [
    id 4
    label 5
    disk 4
    cpu 4
    memory 12
  ]
  node [
    id 5
    label 6
    disk 6
    cpu 3
    memory 7
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 27
    bw 82
  ]
  edge [
    source 0
    target 1
    delay 34
    bw 163
  ]
  edge [
    source 0
    target 2
    delay 33
    bw 117
  ]
  edge [
    source 0
    target 3
    delay 27
    bw 148
  ]
  edge [
    source 1
    target 4
    delay 33
    bw 141
  ]
  edge [
    source 2
    target 4
    delay 33
    bw 164
  ]
  edge [
    source 3
    target 5
    delay 35
    bw 106
  ]
  edge [
    source 4
    target 5
    delay 33
    bw 170
  ]
]

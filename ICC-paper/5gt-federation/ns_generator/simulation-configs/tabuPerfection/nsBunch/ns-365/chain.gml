graph [
  node [
    id 0
    label 1
    disk 4
    cpu 3
    memory 14
  ]
  node [
    id 1
    label 2
    disk 5
    cpu 4
    memory 9
  ]
  node [
    id 2
    label 3
    disk 1
    cpu 4
    memory 14
  ]
  node [
    id 3
    label 4
    disk 2
    cpu 2
    memory 14
  ]
  node [
    id 4
    label 5
    disk 4
    cpu 4
    memory 1
  ]
  node [
    id 5
    label 6
    disk 8
    cpu 2
    memory 4
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 33
    bw 98
  ]
  edge [
    source 0
    target 1
    delay 25
    bw 164
  ]
  edge [
    source 1
    target 2
    delay 28
    bw 182
  ]
  edge [
    source 1
    target 3
    delay 28
    bw 158
  ]
  edge [
    source 2
    target 4
    delay 32
    bw 70
  ]
  edge [
    source 4
    target 5
    delay 28
    bw 109
  ]
]
